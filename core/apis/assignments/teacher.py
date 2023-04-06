from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment
from core.libs import assertions

from .schema import AssignmentSchema, AssignmentGradeSchema
teacher_assignments_resources = Blueprint('teacher_assignments_resources', __name__)

@teacher_assignments_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.auth_principal
def list_assignments(p):
    """Returns list of submitted assignments to teacher"""

    # checking if valid id was provided of not such as "1 2" is invalid but "12" is valid
    try:
        teacher_id=int(p.teacher_id)
    except:
        assertions.id_assert(400,"Teacher ID is not integer")
    submitted_assignments = Assignment.get_assignments_submitted_to_teacher(teacher_id)
    if len(submitted_assignments)==0:
        # Using the status code 601 for handling exceptions when no assignmnet is submitted to the teacher
        assertions.data_assert(601,"No Submitted Assignments")
    submitted_assignments_dump = AssignmentSchema().dump(submitted_assignments, many=True)
    return APIResponse.respond(data=submitted_assignments_dump)

@teacher_assignments_resources.route('/assignments/grade', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
@decorators.auth_principal
def grade_assignment(p, incoming_payload):
    
    # checking if valid id was provided of not such as "1 2" is invalid but "12" is valid
    try:
        p.teacher_id=int(p.teacher_id)
    except:
        assertions.id_assert(400,"Teacher ID is not integer")
    grade_assignment_payload=AssignmentGradeSchema().load(incoming_payload)
    graded_assignment=Assignment._grade(
        _id=grade_assignment_payload.id,
        principal=p,
        grade=grade_assignment_payload.grade
    )

    db.session.commit()
    graded_assignment_dump=AssignmentSchema().dump(graded_assignment)
    return APIResponse.respond(data=graded_assignment_dump)