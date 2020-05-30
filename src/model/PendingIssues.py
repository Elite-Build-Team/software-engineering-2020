# -*- coding: UTF-8 -*-
from typing import List
from model import ReportIssue

class PendingIssues(object):
    def get_pending_issues(self) -> List[ReportIssue]:
        return self.__pending_issues

    def set_pending_issues(self, pending_issues: List[ReportIssue]):
        self.__pending_issues = pending_issues

    def add_pending_issue(self, pending_issue: ReportIssue, ReportIssue.__id):
        self.__pending_issues.append(pending_issue)
        self.__in_pending = True

    def delete_pending_issue(self, pending_issue: ReportIssue):
        self.__pending_issues.remove(pending_issue)

    def get_issue_details(self):
        ReportIssue.get_issue_details()

    def __init__(self):
        self.__pending_issues: List[ReportIssue] = []