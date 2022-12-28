from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, Admin_Emails, User_offers



# class AccountAdmin(UserAdmin):
# 	list_display = ('email','first_name', 'last_name','date_joined', 'last_login', 'is_admin')
# 	search_fields = ('email','first_name',)
# 	readonly_fields=('id', 'date_joined', 'last_login')

# 	filter_horizontal = ()
# 	list_filter = ()
# 	fieldsets = ()


admin.site.register(Account)
admin.site.register(Admin_Emails)


class User_offersAdmin(admin.ModelAdmin):
	list_display = ('name', 'url_text','url')
	search_fields = ('name',)

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()
admin.site.register(User_offers,User_offersAdmin)