"""empty message

Revision ID: ff63e705e3a4
Revises: d4ef3547a228
Create Date: 2021-08-20 01:44:50.225596

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff63e705e3a4'
down_revision = 'd4ef3547a228'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contrato',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_project', sa.String(length=60), nullable=False),
    sa.Column('region', sa.String(length=100), nullable=False),
    sa.Column('comuna', sa.String(length=100), nullable=False),
    sa.Column('sector', sa.String(length=100), nullable=False),
    sa.Column('cerco_geo_latitud', sa.String(length=120), nullable=False),
    sa.Column('cerco_geo_longitud', sa.String(length=120), nullable=False),
    sa.Column('plano', sa.String(length=120), nullable=False),
    sa.Column('obra_descripcion', sa.String(length=200), nullable=False),
    sa.Column('planta_matriz', sa.String(length=120), nullable=False),
    sa.Column('hp', sa.Integer(), nullable=False),
    sa.Column('comentario', sa.String(length=120), nullable=False),
    sa.Column('prioridad', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id_project')
    )
    op.create_table('ordentrabajo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tipo', sa.String(length=100), nullable=False),
    sa.Column('descripcion', sa.String(length=255), nullable=False),
    sa.Column('id_contrato', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_contrato'], ['contrato.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('detalleordentrabajo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tipo', sa.String(length=100), nullable=False),
    sa.Column('descripcion', sa.String(length=255), nullable=False),
    sa.Column('id_ordentrabajo', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_ordentrabajo'], ['ordentrabajo.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('userorden',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=True),
    sa.Column('id_orden', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_orden'], ['ordentrabajo.id'], ),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('acreditacion',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url_foto', sa.String(length=255), nullable=False),
    sa.Column('descripcion', sa.String(length=255), nullable=False),
    sa.Column('id_userorden', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_userorden'], ['userorden.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('statusorden',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('inicio_fecha', sa.String(length=100), nullable=False),
    sa.Column('final_fecha', sa.String(length=100), nullable=True),
    sa.Column('status', sa.String(length=120), nullable=False),
    sa.Column('minutostrabajados', sa.String(length=120), nullable=False),
    sa.Column('url_foto_epp', sa.String(length=120), nullable=False),
    sa.Column('url_foto_referencia', sa.String(length=200), nullable=False),
    sa.Column('geo_lat', sa.String(length=120), nullable=False),
    sa.Column('geo_lon', sa.String(length=120), nullable=False),
    sa.Column('id_userorden', sa.Integer(), nullable=True),
    sa.Column('id_contrato', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_contrato'], ['contrato.id'], ),
    sa.ForeignKeyConstraint(['id_userorden'], ['userorden.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('user', sa.Column('contact', sa.String(length=120), nullable=False))
    op.add_column('user', sa.Column('fecha_nacimiento', sa.String(length=200), nullable=False))
    op.add_column('user', sa.Column('lastname', sa.String(length=100), nullable=False))
    op.add_column('user', sa.Column('name', sa.String(length=100), nullable=False))
    op.add_column('user', sa.Column('perfil', sa.String(length=120), nullable=False))
    op.add_column('user', sa.Column('register', sa.String(length=120), nullable=False))
    op.add_column('user', sa.Column('rut', sa.String(length=12), nullable=False))
    op.drop_constraint('user_email_key', 'user', type_='unique')
    op.drop_column('user', 'is_active')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.create_unique_constraint('user_email_key', 'user', ['email'])
    op.drop_column('user', 'rut')
    op.drop_column('user', 'register')
    op.drop_column('user', 'perfil')
    op.drop_column('user', 'name')
    op.drop_column('user', 'lastname')
    op.drop_column('user', 'fecha_nacimiento')
    op.drop_column('user', 'contact')
    op.drop_table('statusorden')
    op.drop_table('acreditacion')
    op.drop_table('userorden')
    op.drop_table('detalleordentrabajo')
    op.drop_table('ordentrabajo')
    op.drop_table('contrato')
    # ### end Alembic commands ###
