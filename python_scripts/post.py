import facebook
graph = facebook.GraphAPI('EAALoXCL7DgoBAAtp9n7PIxoTYvrnqeyxY9EG99klH00PXWddefYSdu2Q9Li2PTMqjzD5jf4wWYXb9CWWXXDBRX7t45pJAxP21I9TyeSLomkAZATHVTDE18IuZCSVMXBwavBZAa5UyQnniRNdmZCcblXpJWbnp76A0njKUe1EX4N3yxQk7YY4')
# Writes 'Hello, world' to the active user's wall.
graph.put_object(parent_object='me', connection_name='feed',
                 message='Hello, world')