"""
This module is mainly used by Alembic
It imports all database models to be able to create all related tables
"""

import ibims.orm.models  # noqa # pylint: disable=unused-import

# Import all the models, so that Base has them before being
# imported by the create_db function.
from ibims.orm.db.base_class import MappingBase, mapper_registry  # noqa # pylint: disable=unused-import
