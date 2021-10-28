from sqlalchemy import Column, ForeignKey, Integer, String, Sequence, DateTime, UniqueConstraint, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import Schema, fields

Base = declarative_base()
metadata_obj = MetaData()


class COLUMN_VARIANTS(Base):
    __tablename__ = 'COLUMN_VARIANTS'
    district = Column(String(250), nullable=False)
    garage = Column(String(250), nullable=False)
    sheet_id = Column(String(250), nullable=False)
    sheet_title = Column(String(250), nullable=False)
    column_title = Column(String(250), nullable=False)
    column_id = Column(String(250), primary_key=True)
    variant_type = Column(String(250), nullable=False)
    expectation = Column(String(250), nullable=False)
    found = Column(String(250), nullable=False)
    date_added = Column(DateTime, nullable=False)


class ColumnVariantSchema(SQLAlchemySchema):
    class Meta:
        model = COLUMN_VARIANTS
        load_instance = True  # Optional: deserialize to model instances

    district = auto_field()
    garage = auto_field()
    sheet_id = auto_field()
    sheet_title = auto_field()
    column_title = auto_field()
    column_id = auto_field()
    variant_type = auto_field()
    expectation = auto_field()
    found = auto_field()
    date_added = auto_field()


class COLUMN_VARIATIONS_SUMMARY(Base):
    __tablename__ = 'COLUMN_VARIATIONS_SUMMARY'
    variant_type = Column(String(250), primary_key=True)
    variant_count = Column(String(250), nullable=False)


class ColumnVariantSchema(SQLAlchemySchema):
    class Meta:
        model = COLUMN_VARIATIONS_SUMMARY
        load_instance = True  # Optional: deserialize to model instances

    variant_type = auto_field()
    variant_count = auto_field()


class INACTIVE_LICENSED_USERS(Base):
    __tablename__ = 'INACTIVE_LICENSED_USERS'
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), primary_key=True)
    sheet_count = Column(String(250), nullable=False)
    last_login = Column(DateTime, nullable=False)


class InactiveLicensedUserSchema(SQLAlchemySchema):
    class Meta:
        model = INACTIVE_LICENSED_USERS
        load_instance = True  # Optional: deserialize to model instances

    first_name = auto_field()
    last_name = auto_field()
    email = auto_field()
    sheet_count = auto_field()
    last_login = auto_field()


class USER_OWNERSHIP_COUNT(Base):
    __tablename__ = 'SHEET_OWNERSHIP_COUNT'
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), primary_key=True)
    sheet_count = Column(String(250), nullable=False)


class UserOwnershipSheetCountSchema(SQLAlchemySchema):
    class Meta:
        model = INACTIVE_LICENSED_USERS
        load_instance = True  # Optional: deserialize to model instances

    first_name = auto_field()
    last_name = auto_field()
    email = auto_field()
    sheet_count = auto_field()
    last_login = auto_field()


class ADMIN_USERS(Base):
    __tablename__ = 'ADMIN_USERS'
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), primary_key=True)
    last_login = Column(DateTime, nullable=False)


class AdminUserSchema(SQLAlchemySchema):
    class Meta:
        model = ADMIN_USERS
        load_instance = True

    first_name = auto_field()
    last_name = auto_field()
    email = auto_field()
    last_login = auto_field()


user_actions_model = Table('USER_ACTIONS', metadata_obj,
                        Column('ID', String),
                        Column('USER_ID', String),
                        Column('ACCESS_TOKEN', String),
                        Column('ACTION', String),
                        Column('EVENT_TS', String),
                        Column('OBJECT_ID', String),
                        Column('OBJECT_TYPE', String),
                        Column('SOURCE', String),
                        )


design_sheets_model = Table('DESIGN_SHEETS', metadata_obj,
                      Column('SHEET_ID', String),
                      Column('ROW_ID', String),
                      Column('WORK_REQUEST', String),
                      Column('CATEGORY', String),
                      Column('STATUS', String),
                      Column('HELPER', String),
                      Column('CREW', String),
                      Column('OTHER_GARAGE_PERFORMING_WORK', String),
                      Column('ASSIGNED_TO_CREW_FOREMAN', String),
                      Column('CONSTRUCTION_BASELINE_START', String),
                      Column('CONSTRUCTION_BASELINE_END', String),
                      Column('CONSTRUCTION_PLANNED_START', String),
                      Column('CONSTRUCTION_PLANNED_END', String),
                      Column('CONSTRUCTION_ACTUAL_START', String),
                      Column('CONSTRUCTION_ACTUAL_END', String),
                      Column('CONSTRUCTION_END_QTR', String),
                      Column('SCHEDULE_BREAK_REASON', String),
                      Column('SCHEDULE_BREAK_COMMENT', String),
                      Column('CONSTRUCTION_START_VARIANCE', String),
                      Column('CONSTRUCTION_END_VARIANCE', String),
                      Column('WORK_REQUEST_DESCRIPTION', String),
                      Column('WORK_ORDER', String),
                      Column('PARENT_WORK_REQUEST', String),
                      Column('CIRCUIT_NAME', String),
                      Column('ADDRESS', String),
                      Column('CUSTOMER', String),
                      Column('CONTACT', String),
                      Column('CREATED_BY', String),
                      Column('CREATE_DATE', String),
                      Column('DATE_REQUIRED', String),
                      Column('NSD_DATE', String),
                      Column('ASSIGNED_TO', String),
                      Column('CONSTRUCTION_AEP___CONTRACTOR', String),
                      Column('BUSINESS_PARTNER_REFERENCE_NUMBER', String),
                      Column('NUMBER_OF_NEW_EASEMENTS', String),
                      Column('NUMBER_OF_EASEMENTS_ACQUIRED', String),
                      Column('OUPS_EXPIRATION_DATE', String),
                      Column('MATERIAL_STAGING', String),
                      Column('ESTIMATE_HOURS', String),
                      Column('WEEKS_CONSTRUCTION', String),
                      Column('ON_HOLD_CONSTRUCTION', String),
                      Column('PERCENT_CONSTRUCTION_COMPLETE', String),
                      Column('REMAINING_WEEKS_CONSTRUCTION', String),
                      Column('AT_RISK', String),
                      Column('DURATION', String),
                      Column('PREDECESSORS', String),
                      Column('AS_BUILT_HOURS', String),
                      Column('CREW_HEADQUARTERS', String),
                      Column('JOBTYPE', String),
                      Column('PROJECT_ID', String),
                      Column('WBS_LVL_2', String),
                      Column('BUCKET', String),
                      Column('WBS_LVL_3', String),
                      Column('CONTRACTOR_CODE', String),
                      Column('ASSIGNED_TO_EMAIL', String),
                      Column('URD_PERCENTAGE_BORED', String),
                      Column('URD_PERCENTAGE_TERMINATED', String),
                      Column('WORK_REQUEST_COMMENT', String),
                      Column('COST_EST_TOTAL_CONSTRUCTION', String),
                      Column('COST_EST_TOTAL_RETIREMENT', String),
                      Column('COST_EST_TOTAL_MAINTENANCE', String),
                      Column('MATERIAL_REQUISITION_DATE', String),
                      Column('MATERIAL_NEED_BY_DATE', String),
                      Column('MATERIAL_STAGED_DATE', String),
                      Column('OUPS', String),
                      Column('JOB_NOTES', String),
                      Column('ENGINEERING_PLANNED_START_DATE', String),
                      Column('ENGINEERING_PLANNED_END_DATE', String),
                      Column('JSH_EV', String),
                      Column('ENGINEERING_ACTUAL_FORECAST_START', String),
                      Column('ENGINEERING_ACTUAL_FORECAST_END', String),
                      Column('ENGINEERING_ASSIGNMENT', String),
                      Column('ENGINEERING_PERCENT_COMPLETE', String),
                      Column('ENGINEERING_EARNED_HOURS', String),
                      Column('ENGINEERING_STATUS', String),
                      Column('DESIGN_PLANNED_START_DATE', String),
                      Column('DESIGN_PLANNED_END_DATE', String),
                      Column('DESIGN_ACTUAL_FORECAST_START', String),
                      Column('DESIGN_ACTUAL_FORECAST_END', String),
                      Column('DESIGN_ASSIGNMENT', String),
                      Column('DESIGN_PERCENT_COMPLETE', String),
                      Column('DESIGN_STATUS', String),
                      Column('ROW_PLANNED_START_DATE', String),
                      Column('ROW_PLANNED_END_DATE', String),
                      Column('ROW_ACTUAL_FORECAST_START', String),
                      Column('ROW_ACTUAL_FORECAST_END', String),
                      Column('ROW_ASSIGNMENT', String),
                      Column('ROW_PERCENT_COMPLETE', String),
                      Column('ROW_STATUS', String),
                      Column('FORESTRY_PLANNED_START_DATE', String),
                      Column('FORESTRY_PLANNED_END_DATE', String),
                      Column('FORESTRY_ACTUAL_FORECAST_START', String),
                      Column('FORESTRY_ACTUAL_FORECAST_END', String),
                      Column('FORESTRY_ASSIGNMENT', String),
                      Column('FORESTRY_PERCENT_COMPLETE', String),
                      Column('COMMENTS', String),
                      Column('LONG_LEAD_MATERIAL_ARRIVAL_DATE', String),
                      Column('FORESTRY_STATUS', String),
                      Column('PERMIT_START_DATE', String),
                      Column('PERMIT_EXPIRATION_DATE', String),
                      Column('PERMIT_CATEGORY', String),
                      Column('RANKING', String),
                      Column('COUNTY', String),
                      Column('IMPORTED_PARAMETRIC_COST_LOADED', String),
                      Column('IMPORTED_ESTIMATE_BUDGET_HOURS', String),
                      Column('SEVENOSEVEN_COMPLETE_DATE', String),
                      Column('PARAMETRIC_FACTOR_COST', String),
                      Column('PARAMETRIC_FACTOR_JSH', String),
                      Column('CONSTRUCTION_TYPE_OH_UG_NETWORK', String),
                      Column('UNITS', String),
                      Column('CIRCUIT_ENGINEER', String),
                      Column('PARAMETRIC_COST_LOADED', String),
                      Column('FACE_SHEET_COST', String),
                      Column('WORK_PLAN_YEAR', String),
                      Column('WORK_PLAN_YEAR_IS_CURRENT_YEAR', String),
                      Column('EARNED_UNITS', String),
                      Column('ESTIMATE_BUDGET_HOURS', String),
                      Column('PLANNED_HOURS', String),
                      Column('EARNED_BUDGET_HOURS', String),
                      Column('ACTUAL_HOURS', String),
                      Column('JSH_EAC', String),
                      Column('CONSTRUCTION_SCHEDULE_VARIANCE', String),
                      Column('ENGINEERING_START_VARIANCE', String),
                      Column('ENGINEERING_END_VARIANCE', String),
                      Column('DESIGN_START_VARIANCE', String),
                      Column('DESIGN_END_VARIANCE', String),
                      Column('ROW_START_VARIANCE', String),
                      Column('ROW_END_VARIANCE', String),
                      Column('FORESTRY_START_VARIANCE', String),
                      Column('FORESTRY_END_VARIANCE', String),
                      Column('COST_VARIANCE', String),
                      Column('JSH_VARIANCE', String),
                      Column('TODAY_', String),
                      Column('START_MONTH', String),
                      Column('SPI', String),
                      Column('SURVEY_STAKING_STATUS', String),
                      Column('REDLINES_RETURNED_FROM_BP', String),
                      Column('REDLINES_ACKNOWLEDGED_BY_INSPECTOR', String),
                      Column('SENT_TO_INFORMATION_SYSTEMS', String),
                      Column('INFOSYS_REQUEST_INFO_FROM', String),
                      Column('PRE_CONSTRUCTION_HEALTH', String),
                      Column('INFOSYS_REQUEST_INFO_DATE', String),
                      Column('INFOSYS_REQUEST_INFO_TYPE', String),
                      Column('INFOSYS_REQUESTED_INFO_RECEIVED', String),
                      Column('ESTIMATED_COSTS', String),
                      Column('MATERIAL_BACKORDER_LIST', String),
                      Column('ACTUAL_MATERIAL_COSTS', String),
                      Column('ACTUAL_LABOR_COSTS', String),
                      Column('ACTUAL_TOTAL_COSTS', String),
                      Column('FORESTRY_HEALTH', String),
                      Column('ASB_BO_REPORT_AEP', String),
                      Column('MRO_PLAN_NEED_DATE', String),
                      Column('ASB_CONTRACTOR_APPROVED', String),
                      Column('MRO_REQUIRED', String),
                      Column('BOT_UPDATE', String)
                      )

design_sheet_column_mapping = {'District': 'DISTRICT',
                   'Row ID': 'ROW_ID',
                   'Work Request': 'WORK_REQUEST',
                   'Category': 'CATEGORY',
                   'Status': 'STATUS',
                   'Helper': 'HELPER',
                   'Crew': 'CREW',
                   'Other Garage Performing Work': 'OTHER_GARAGE_PERFORMING_WORK',
                   'Assigned To (Crew) / Foreman': 'ASSIGNED_TO_CREW_FOREMAN',
                   'Construction Baseline Start': 'CONSTRUCTION_BASELINE_START',
                   'Construction Baseline End': 'CONSTRUCTION_BASELINE_END',
                   'Construction Planned Start': 'CONSTRUCTION_PLANNED_START',
                   'Construction Planned End': 'CONSTRUCTION_PLANNED_END',
                   'Construction Actual Start': 'CONSTRUCTION_ACTUAL_START',
                   'Construction Actual End': 'CONSTRUCTION_ACTUAL_END',
                   'Construction End QTR': 'CONSTRUCTION_END_QTR',
                   'Schedule Break Reason': 'SCHEDULE_BREAK_REASON',
                   'Schedule Break Comment': 'SCHEDULE_BREAK_COMMENT',
                   'Construction Start Variance': 'CONSTRUCTION_START_VARIANCE',
                   'Construction End Variance': 'CONSTRUCTION_END_VARIANCE',
                   'Work Request Description': 'WORK_REQUEST_DESCRIPTION',
                   'Work Order': 'WORK_ORDER',
                   'Parent Work Request': 'PARENT_WORK_REQUEST',
                   'Circuit Name': 'CIRCUIT_NAME',
                   'Address': 'ADDRESS',
                   'Customer': 'CUSTOMER',
                   'Contact': 'CONTACT',
                   'Created By': 'CREATED_BY',
                   'Create Date': 'CREATE_DATE',
                   'Date Required': 'DATE_REQUIRED',
                   'NSD Date': 'NSD_DATE',
                   'Assigned To': 'ASSIGNED_TO',
                   'Construction AEP / Contractor': 'CONSTRUCTION_AEP___CONTRACTOR',
                   'Business Partner Reference Number': 'BUSINESS_PARTNER_REFERENCE_NUMBER',
                   'Number of New Easements': 'NUMBER_OF_NEW_EASEMENTS',
                   'Number of Easements Acquired': 'NUMBER_OF_EASEMENTS_ACQUIRED',
                   'OUPS Expiration Date': 'OUPS_EXPIRATION_DATE',
                   'Material Staging': 'MATERIAL_STAGING',
                   'Estimate Hours': 'ESTIMATE_HOURS',
                   'Weeks Construction': 'WEEKS_CONSTRUCTION',
                   'On Hold Construction': 'ON_HOLD_CONSTRUCTION',
                   'Percent Construction Complete': 'PERCENT_CONSTRUCTION_COMPLETE',
                   'Remaining Weeks Construction': 'REMAINING_WEEKS_CONSTRUCTION',
                   'AT Risk': 'AT_RISK',
                   'Duration': 'DURATION',
                   'Predecessors': 'PREDECESSORS',
                   'As-built Hours': 'AS_BUILT_HOURS',
                   'Crew Headquarters': 'CREW_HEADQUARTERS',
                   'Jobtype': 'JOBTYPE',
                   'Project ID': 'PROJECT_ID',
                   'WBS LVL 2': 'WBS_LVL_2',
                   'Bucket': 'BUCKET',
                   'WBS LVL 3': 'WBS_LVL_3',
                   'Contractor Code': 'CONTRACTOR_CODE',
                   'Assigned To Email': 'ASSIGNED_TO_EMAIL',
                   'URD % Bored': 'URD_PERCENTAGE_BORED',
                   'URD % Terminated': 'URD_PERCENTAGE_TERMINATED',
                   'Work Request Comment': 'WORK_REQUEST_COMMENT',
                   'Cost Est Total Construction': 'COST_EST_TOTAL_CONSTRUCTION',
                   'Cost Est Total Retirement': 'COST_EST_TOTAL_RETIREMENT',
                   'Cost Est Total Maintenance': 'COST_EST_TOTAL_MAINTENANCE',
                   'Material Requisition Date': 'MATERIAL_REQUISITION_DATE',
                   'Material Need By Date': 'MATERIAL_NEED_BY_DATE',
                   'Material Staged Date': 'MATERIAL_STAGED_DATE',
                   'OUPS#': 'OUPS',
                   'Job Notes': 'JOB_NOTES',
                   'Engineering Planned Start Date': 'ENGINEERING_PLANNED_START_DATE',
                   'Engineering Planned End Date': 'ENGINEERING_PLANNED_END_DATE',
                   'JSH EV': 'JSH_EV',
                   'Engineering Actual/Forecast Start': 'ENGINEERING_ACTUAL_FORECAST_START',
                   'Engineering Actual/Forecast End': 'ENGINEERING_ACTUAL_FORECAST_END',
                   'Engineering Assignment': 'ENGINEERING_ASSIGNMENT',
                   'Engineering Percent Complete': 'ENGINEERING_PERCENT_COMPLETE',
                   'Engineering Earned Hours': 'ENGINEERING_EARNED_HOURS',
                   'Engineering Status': 'ENGINEERING_STATUS',
                   'Design Planned Start Date': 'DESIGN_PLANNED_START_DATE',
                   'Design Planned End Date': 'DESIGN_PLANNED_END_DATE',
                   'Design Actual/Forecast Start': 'DESIGN_ACTUAL_FORECAST_START',
                   'Design Actual/Forecast End': 'DESIGN_ACTUAL_FORECAST_END',
                   'Design Assignment': 'DESIGN_ASSIGNMENT',
                   'Design Percent Complete': 'DESIGN_PERCENT_COMPLETE',
                   'Design Status': 'DESIGN_STATUS',
                   'ROW Planned Start Date': 'ROW_PLANNED_START_DATE',
                   'ROW Planned End Date': 'ROW_PLANNED_END_DATE',
                   'ROW Actual/Forecast Start': 'ROW_ACTUAL_FORECAST_START',
                   'ROW Actual/Forecast End': 'ROW_ACTUAL_FORECAST_END',
                   'ROW Assignment': 'ROW_ASSIGNMENT',
                   'ROW Percent Complete': 'ROW_PERCENT_COMPLETE',
                   'ROW Status': 'ROW_STATUS',
                   'Forestry Planned Start Date': 'FORESTRY_PLANNED_START_DATE',
                   'Forestry Planned End Date': 'FORESTRY_PLANNED_END_DATE',
                   'Forestry Actual/Forecast Start': 'FORESTRY_ACTUAL_FORECAST_START',
                   'Forestry Actual/Forecast End': 'FORESTRY_ACTUAL_FORECAST_END',
                   'Forestry Assignment': 'FORESTRY_ASSIGNMENT',
                   'Forestry Percent Complete': 'FORESTRY_PERCENT_COMPLETE',
                   'Comments': 'COMMENTS',
                   'Long Lead Material Arrival Date': 'LONG_LEAD_MATERIAL_ARRIVAL_DATE',
                   'Forestry Status': 'FORESTRY_STATUS',
                   'Permit Start Date': 'PERMIT_START_DATE',
                   'Permit Expiration Date': 'PERMIT_EXPIRATION_DATE',
                   'Permit Category': 'PERMIT_CATEGORY',
                   'Work Plan Changes Comments': 'WORK_PLAN_CHANGES_COMMENTS',
                   'Ranking': 'RANKING',
                   'County': 'COUNTY',
                   'Imported Parametric Cost Loaded': 'IMPORTED_PARAMETRIC_COST_LOADED',
                   'Imported Estimate Budget Hours': 'IMPORTED_ESTIMATE_BUDGET_HOURS',
                   '707 Complete Date': 'SEVENOSEVEN_COMPLETE_DATE',
                   'Parametric Factor Cost': 'PARAMETRIC_FACTOR_COST',
                   'Parametric Factor JSH': 'PARAMETRIC_FACTOR_JSH',
                   'Construction Type OH/UG/Network': 'CONSTRUCTION_TYPE_OH_UG_NETWORK',
                   'Units': 'UNITS',
                   'Circuit Engineer': 'CIRCUIT_ENGINEER',
                   'Parametric Cost Loaded': 'PARAMETRIC_COST_LOADED',
                   'Face Sheet Cost': 'FACE_SHEET_COST',
                   'Work Plan Year': 'WORK_PLAN_YEAR',
                   'Work Plan Year is Current Year?': 'WORK_PLAN_YEAR_IS_CURRENT_YEAR',
                   'Earned Units': 'EARNED_UNITS',
                   'Estimate Budget Hours': 'ESTIMATE_BUDGET_HOURS',
                   'Planned Hours': 'PLANNED_HOURS',
                   'Earned Budget Hours': 'EARNED_BUDGET_HOURS',
                   'Actual Hours': 'ACTUAL_HOURS',
                   'JSH EAC': 'JSH_EAC',
                   'Construction Schedule Variance': 'CONSTRUCTION_SCHEDULE_VARIANCE',
                   'Engineering Start Variance': 'ENGINEERING_START_VARIANCE',
                   'Engineering End Variance': 'ENGINEERING_END_VARIANCE',
                   'Design Start Variance': 'DESIGN_START_VARIANCE',
                   'Design End Variance': 'DESIGN_END_VARIANCE',
                   'ROW Start Variance': 'ROW_START_VARIANCE',
                   'ROW End Variance': 'ROW_END_VARIANCE',
                   'Forestry Start Variance': 'FORESTRY_START_VARIANCE',
                   'Forestry End Variance': 'FORESTRY_END_VARIANCE',
                   'Cost Variance': 'COST_VARIANCE',
                   'JSH Variance': 'JSH_VARIANCE',
                   'Today': 'TODAY_',
                   'Start Month': 'START_MONTH',
                   'SPI': 'SPI',
                   'Survey Staking Status': 'SURVEY_STAKING_STATUS',
                   'RedLines Returned from BP': 'REDLINES_RETURNED_FROM_BP',
                   'RedLines Acknowledged by Inspector': 'REDLINES_ACKNOWLEDGED_BY_INSPECTOR',
                   'Sent to Information Systems': 'SENT_TO_INFORMATION_SYSTEMS',
                   'InfoSys Request Info From': 'INFOSYS_REQUEST_INFO_FROM',
                   'Pre-Construction Health': 'PRE_CONSTRUCTION_HEALTH',
                   'InfoSys Request Info Date': 'INFOSYS_REQUEST_INFO_DATE',
                   'InfoSys Request Info Type': 'INFOSYS_REQUEST_INFO_TYPE',
                   'InfoSys Requested Info Received': 'INFOSYS_REQUESTED_INFO_RECEIVED',
                   'Estimated Costs': 'ESTIMATED_COSTS',
                   'Material Backorder List': 'MATERIAL_BACKORDER_LIST',
                   'Actual Material Costs': 'ACTUAL_MATERIAL_COSTS',
                   'Actual Labor Costs': 'ACTUAL_LABOR_COSTS',
                   'Actual Total Costs': 'ACTUAL_TOTAL_COSTS',
                   'Forestry Health': 'FORESTRY_HEALTH',
                   'ASB BO Report AEP': 'ASB_BO_REPORT_AEP',
                   'MRO Plan Need Date': 'MRO_PLAN_NEED_DATE',
                   'ASB Contractor Approved': 'ASB_CONTRACTOR_APPROVED',
                   'MRO Required': 'MRO_REQUIRED',
                   'BOT Update': 'BOT_UPDATE'}