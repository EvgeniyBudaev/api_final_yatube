from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class PostsPagination(LimitOffsetPagination):
    default_limit = 2

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.count,
            'response': data
        })
