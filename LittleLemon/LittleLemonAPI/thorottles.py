from rest_framework.throttling import UserRateThrottle


class TenCallsPerMin(UserRateThrottle):
    scope = "ten"
    rate = "10/min"
