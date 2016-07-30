from django.conf.urls import url
import django_sb_admin_ssx.views

urlpatterns = [
    url(r'^$', django_sb_admin_ssx.views.start, name='sb_admin_start'),
    url(r'^dashboard/$', django_sb_admin_ssx.views.dashboard, name='sb_admin_dashboard'),
    url(r'^charts/$', django_sb_admin_ssx.views.charts, name='sb_admin_charts'),
    url(r'^tables/$', django_sb_admin_ssx.views.tables, name='sb_admin_tables'),
    url(r'^forms/$', django_sb_admin_ssx.views.forms, name='sb_admin_forms'),
    url(r'^bootstrap-elements/$', django_sb_admin_ssx.views.bootstrap_elements, name='sb_admin_bootstrap_elements'),
    url(r'^bootstrap-grid/$', django_sb_admin_ssx.views.bootstrap_grid, name='sb_admin_bootstrap_grid'),
    url(r'^rtl-dashboard/$', django_sb_admin_ssx.views.rtl_dashboard, name='sb_admin_rtl_dashboard'),
    url(r'^blank/$', django_sb_admin_ssx.views.blank, name='sb_admin_blank'),
]