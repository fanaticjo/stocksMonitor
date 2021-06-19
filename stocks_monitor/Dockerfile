FROM public.ecr.aws/lambda/python:3.6
COPY src ./
COPY req.txt ./
RUN pip install -r req.txt
CMD ["run.app"]