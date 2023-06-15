from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination, CursorPagination

class ProductPagination(PageNumberPagination):
    page_size=2 #total no of content in each page
    page_query_param="p"
    page_size_query_param = "size" # we have defined that each page contain 2 content. but by using this user can change
    max_page_size = 2 #how many page can show. it depends on page_size_query_param
    
    
    
class ProductLimitOffset(LimitOffsetPagination):
    default_limit=2 #by default limit will be 2
    limit_query_param="l" #limit name as l
    offset_query_param="o" #offset name as o
    max_limit=3 # if I give limit =4  , then it will not show 4 content. it will show max 3 content
    
    
    
    
class ProductCursor(CursorPagination):
    page_size=2 # total no of content in each page
    ordering="name" # we must have to give ordering