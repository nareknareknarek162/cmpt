from django.db import models
from viewflow import fsm


class State(models.TextChoices):
    ON_MODERATION = "on_moderation"
    APPROVED = "approved"
    ON_DELETE = "on_delete"
    REJECTED = "rejected"


class Flow:
    state = fsm.State(State, default=State.ON_MODERATION)

    def __init__(self, object):
        self.object = object

    @state.setter()
    def _set_object_state(self, value):
        self.object.state = value

    @state.getter()
    def _get_object_state(self):
        return self.object.state

    @state.on_success()
    def _on_transition_success(self, descriptor, source, target):
        self.object.save()

    @state.transition(source=State.ON_MODERATION, target=State.APPROVED)
    def approve(self):
        pass

    @state.transition(source=State.ON_MODERATION, target=State.REJECTED)
    def reject(self):
        pass

    @state.transition(
        source=(State.ON_MODERATION, State.APPROVED, State.REJECTED),
        target=State.ON_DELETE,
    )
    def delete(self):
        pass

    @state.transition(
        source=(State.APPROVED, State.REJECTED, State.ON_DELETE),
        target=State.ON_MODERATION,
    )
    def edit(self):
        pass
