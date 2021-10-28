from django.conf import settings
from django.contrib import admin

from django_simple_coupons.models import (Coupon,
                                          Discount,
                                          Ruleset,
                                          CouponUser,
                                          AllowedUsersRule,
                                          MaxUsesRule,
                                          ValidityRule)

from django_simple_coupons.actions import (reset_coupon_usage, delete_expired_coupons)


# Register your models here.
# ==========================
@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'ruleset', 'times_used', 'applicable_to', 'created', )
    actions = [delete_expired_coupons]

    fieldsets = [
        (None, {"fields": ["code", "discount", "ruleset", "times_used", "created"]}),
        (
            "This Coupon Applicable To",
            {
                "fields": ["applicable_to"],
                "description": f"Purchasable objects comma separated. Options: {', '.join(settings.PURCHASABLE_OBJECTS.values())}",
            },
        ),
    ]
    readonly_fields = [
        "times_used",
        "created"
    ]


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    pass


@admin.register(Ruleset)
class RulesetAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'allowed_users', 'max_uses', 'validity', )


@admin.register(CouponUser)
class CouponUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_user_email', 'get_user_name', 'coupon', 'last_used', 'times_used', )
    actions = [reset_coupon_usage]

    def get_user_email(self, obj):
        return obj.user.email

    get_user_email.short_description = 'User Email'
    get_user_email.admin_order_field = 'user__email'

    def get_user_name(self, obj):
        return obj.user.first_name + " " + obj.user.last_name

    get_user_name.short_description = 'User Name'
    get_user_name.admin_order_field = 'user__first_name'


@admin.register(AllowedUsersRule)
class AllowedUsersRuleAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


@admin.register(MaxUsesRule)
class MaxUsesRuleAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


@admin.register(ValidityRule)
class ValidityRuleAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}
