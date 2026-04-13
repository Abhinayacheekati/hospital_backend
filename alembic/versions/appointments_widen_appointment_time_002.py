"""Widen appointments.appointment_time for normalized HH:MM:SS and safety margin.

Revision ID: appointments_widen_appointment_time_002
Revises: doctor_profile_consultation_fields_001
Create Date: 2026-04-10

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import inspect


revision = "appointments_widen_appointment_time_002"
down_revision = "doctor_profile_consultation_fields_001"
branch_labels = None
depends_on = None


def _table_exists(conn, name: str) -> bool:
    return name in inspect(conn).get_table_names()


def upgrade():
    conn = op.get_bind()
    if not _table_exists(conn, "appointments"):
        return
    op.alter_column(
        "appointments",
        "appointment_time",
        existing_type=sa.String(length=8),
        type_=sa.String(length=16),
        existing_nullable=False,
    )


def downgrade():
    conn = op.get_bind()
    if not _table_exists(conn, "appointments"):
        return
    op.alter_column(
        "appointments",
        "appointment_time",
        existing_type=sa.String(length=16),
        type_=sa.String(length=8),
        existing_nullable=False,
    )
