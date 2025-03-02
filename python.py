
#Creating and Running a Python Script for CPU Utilization Test
mkdir test1
cd test1
v1 test.py


#Infinite Number Generator Using Python Yield
def to_infinity():
    index = 0
    while True:
        yield index
        index += 1

for i in to_infinity():
    if i > 10:
        i1=1

# Press :x and enter will open cmd line 
# run the below commond to check the utilization of CPU 
python3 test.py
