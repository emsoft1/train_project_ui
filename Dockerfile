# $DEL_BEGIN

# ####### 👇 SIMPLE SOLUTION (x86 and M1) 👇 ########
# FROM python:3.8.12-buster

# WORKDIR /prod

# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt

# COPY taxifare taxifare
# COPY setup.py setup.py
# RUN pip install .

# COPY Makefile Makefile
# RUN make reset_local_files

# CMD uvicorn taxifare.api.fast:app --host 0.0.0.0 --port $PORT

####### 👇 OPTIMIZED SOLUTION (x86)👇 #######

# tensorflow base-images are optimized: lighter than python-buster + pip install tensorflow
# FROM tensorflow/tensorflow:2.10.0
# # OR for apple silicon, use this base image instead
# # FROM armswdev/tensorflow-arm-neoverse:r22.09-tf-2.10.0-eigen

# WORKDIR /prod

# # We strip the requirements from useless packages like `ipykernel`, `matplotlib` etc...
# COPY requirements_prod.txt requirements.txt
# RUN pip install -r requirements.txt

# COPY taxifare taxifare
# COPY setup.py setup.py
# RUN pip install .

# COPY Makefile Makefile
# RUN make reset_local_files

# CMD uvicorn taxifare.api.fast:app --host 0.0.0.0 --port $PORT
# $DEL_END
FROM python:3.10.6
EXPOSE 3010
WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
CMD ls
CMD streamlit run  Home.py --server.port 3010
