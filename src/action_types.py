from enum import Enum


class ActionTypes(Enum):
    LOGIN = "login"
    LOGOUT = "logout"
    FORGET_PASS = "forget_pass"
    CREATE_ACC = "create_acc"
    JOIN_TEAM = "join_team"
    LEAVE_TEAM = "leave_team"
    JOIN_COMP = "join_comp"
    LEAVE_COMP = "leave_comp"
    JOIN_PHASE = "join_phase"
    LEAVE_PHASE = "close_phase"
    MAKE_TRIAL = "make_trial"
    SUBMIT_TRIAL = "submit_trial"
    DL_DATASET = "dl_dataset"
    UL_RESULT = "ul_result"
    SUBMIT_REPORT = "submit_report"
    MULTI_CHOICE_CHANGE_ANSWER = "multi_choice_change_answer"
    MULTI_CHOICE_SET_ANSWER = "multi_choice_set_answer"
    MULTI_VALUE_ADD_ANSWER = "multi_value_add_answer"
    MULTI_VALUE_REMOVE_ANSWER = "multi_value_remove_answer"
    VIEW_OLD_PHASE = "view_old_phase"
    VIEW_OLD_TRIAL = "view_old_trial"
    BOOLEAN_SET_ANSWER = "boolean_set_answer"
    BOOLEAN_CHANGE_ANSWER = "boolean_change_answer"

    @classmethod
    def list_types(cls):
        return list(cls._member_map_.keys())
