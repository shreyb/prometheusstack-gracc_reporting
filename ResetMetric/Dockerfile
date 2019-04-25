# CENTOS 7 image
FROM centos:7

# Set up libraries
# Get PIP.  
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
RUN yum -y install python-pip && pip install -U pip 
RUN pip install prometheus_client && pip install requests

# Copy in python executable
COPY reset_metric.py /tmp/reset_metric.py

# Run the executable
CMD ["python", "/tmp/reset_metric.py"]

