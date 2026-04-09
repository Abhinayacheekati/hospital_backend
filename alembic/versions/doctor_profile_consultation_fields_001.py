"""doctor_profiles: consultation_type, availability_time

Revision ID: doctor_profile_consultation_fields_001
Revises: patient_profile_opd_fields_001
Create Date: 2026-04-09

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import inspect


revision = "doctor_profile_consultation_fields_001"
down_revision = "patient_profile_opd_fields_001"
branch_labels = None
depends_on = None


def _table_exists(conn, name: str) -> bool:
    return name in inspect(conn).get_table_names()


def _column_exists(conn, table: str, column: str) -> bool:
    if not _table_exists(conn, table):
        return False
    return column in {c["name"] for c in inspect(conn).get_columns(table)}


def upgrade():
    conn = op.get_bind()
    if not _table_exists(conn, "doctor_profiles"):
        return
    if not _column_exists(conn, "doctor_profiles", "consultation_type"):
        op.add_column(
            "doctor_profiles",
            sa.Column("consultation_type", sa.String(length=100), nullable=True),
        )
    if not _column_exists(conn, "doctor_profiles", "availability_time"):
        op.add_column(
            "doctor_profiles",
            sa.Column("availability_time", sa.Text(), nullable=True),
        )


def downgrade():
    conn = op.get_bind()
    if not _table_exists(conn, "doctor_profiles"):
        return
    if _column_exists(conn, "doctor_profiles", "availability_time"):
        op.drop_column("doctor_profiles", "availability_time")
    if _column_exists(conn, "doctor_profiles", "consultation_type"):
        op.drop_column("doctor_profiles", "consultation_type")
