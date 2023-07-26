FROM apache/airflow:2.6.3

USER root

RUN apt-get update && apt-get install -y \
    r-base \
    r-base-dev

# Optional: Install any additional R packages you may need
# For example:
# RUN R -e "install.packages('package_name')"

# Path where airflow is installed on your local machine
WORKDIR /Users/jay.saini/airflow
