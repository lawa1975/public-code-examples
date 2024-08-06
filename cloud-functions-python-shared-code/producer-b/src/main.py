
import functions_framework

@functions_framework.http
def producer_b_function():
    return 'Here is the producer B function!'
