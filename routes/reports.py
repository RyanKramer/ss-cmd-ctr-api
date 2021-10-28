from flask import Blueprint, redirect, url_for, request, jsonify, session
import json
from routes.utility import resolve_truth
from db_session import dbSession
from models import COLUMN_VARIANTS, COLUMN_VARIATIONS_SUMMARY, INACTIVE_LICENSED_USERS, ADMIN_USERS
import datetime

reports_blueprint = Blueprint('reports', __name__)


@reports_blueprint.route('/api/variance-report', methods=['GET', 'OPTIONS'])
def get_variance_report():
    if request.method == "GET":
        report_name = request.args.get('reportName')

        variants = dbSession.query(COLUMN_VARIANTS).filter(
            COLUMN_VARIANTS.variant_type == report_name)
        modified_variants = []
        for row in variants:
            variant = {}
            variant["district"] = row.district
            variant["garage"] = row.garage
            variant["sheet_id"] = row.sheet_id
            variant["sheet_title"] = row.sheet_title
            variant["column_title"] = row.column_title
            variant["column_id"] = row.column_id
            variant["variant_type"] = row.variant_type
            variant["expectation"] = row.expectation
            variant["found"] = row.found
            variant["date_added"] = row.date_added.strftime("%m/%d/%Y")
            modified_variants.append(variant)
            print(row)

        dump_data = json.dumps(modified_variants)
        if len(dump_data) > 0:
            return jsonify(dump_data)
        else:
            return jsonify([])
    else:
        return ""


@reports_blueprint.route('/api/summary-variance-report', methods=['GET', 'OPTIONS'])
def get_summary_variance_report():
    if request.method == "GET":
        variants = dbSession.query(COLUMN_VARIATIONS_SUMMARY)
        variant_summary = []
        for row in variants:
            variant = {}
            variant["variant_type"] = row.variant_type
            variant["variant_count"] = row.variant_count
            variant_summary.append(variant)

        dump_data = json.dumps(variant_summary)
        if len(dump_data) > 0:
            return jsonify(dump_data)
        else:
            return jsonify([])
    else:
        return ""


@reports_blueprint.route('/api/inactive-licensed-users-report', methods=['GET', 'OPTIONS'])
def get_inactive_licensed_users():
    if request.method == "GET":
        variants = dbSession.query(INACTIVE_LICENSED_USERS)
        inactive_users = []
        for row in variants:
            user = {}
            user["first_name"] = row.first_name
            user["last_name"] = row.last_name
            user["email"] = row.email
            user["sheet_count"] = row.sheet_count
            user["last_login"] = row.last_login.strftime("%m/%d/%Y")
            inactive_users.append(user)

        dump_data = json.dumps(inactive_users)
        if len(dump_data) > 0:
            return jsonify(dump_data)
        else:
            return jsonify([])
    else:
        return ""


@reports_blueprint.route('/api/admin-users-report', methods=['GET', 'OPTIONS'])
def get_admin_users():
    if request.method == "GET":
        variants = dbSession.query(ADMIN_USERS)
        admin_users = []
        for row in variants:
            user = {}
            user["first_name"] = row.first_name
            user["last_name"] = row.last_name
            user["email"] = row.email
            user["last_login"] = row.last_login.strftime("%m/%d/%Y")
            admin_users.append(user)

        dump_data = json.dumps(admin_users)
        if len(dump_data) > 0:
            return jsonify(dump_data)
        else:
            return jsonify([])
    else:
        return ""


@reports_blueprint.route('/api/user-sheet-ownership-count-report', methods=['GET', 'OPTIONS'])
def get_user_sheet_ownership():
    if request.method == "GET":
        variants = dbSession.query(ADMIN_USERS)
        admin_users = []
        for row in variants:
            user = {}
            user["first_name"] = row.first_name
            user["last_name"] = row.last_name
            user["email"] = row.email
            user["last_login"] = row.last_login.strftime("%m/%d/%Y")
            admin_users.append(user)

        dump_data = json.dumps(admin_users)
        if len(dump_data) > 0:
            return jsonify(dump_data)
        else:
            return jsonify([])
    else:
        return ""

# @reports_blueprint.route('/api/variance-reports', methods=['GET', 'OPTIONS'])
# def get_variance_summary_report():
#     if request.method == "GET":
#
#         variants = dbSession.query(COLUMN_VARIANTS).filter(
#             COLUMN_VARIANTS.variant_type == "COLUMN_TYPE")
#         modified_variants = []
#         for row in variants:
#             variant = {}
#             variant["district"] = row.district
#             variant["garage"] = row.garage
#             variant["sheet_id"] = row.sheet_id
#             variant["sheet_title"] = row.sheet_title
#             variant["column_title"] = row.column_title
#             variant["column_id"] = row.column_id
#             variant["variant_type"] = row.variant_type
#             variant["expectation"] = row.expectation
#             variant["found"] = row.found
#             variant["date_added"] = row.date_added.strftime("%m/%d/%Y")
#             modified_variants.append(variant)
#
#         dump_data = json.dumps(modified_variants)
#         if len(dump_data) > 0:
#             return jsonify(dump_data)
#         else:
#             return jsonify([])
#     else:
#         return ""
