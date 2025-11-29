FROM alpine:latest
WORKDIR /opt/
RUN --mount=type=cache,target=/var/cache/apk/ \
    apk add python3 py3-pip py3-uv && \
    /usr/bin/env python3 -m venv ./venv/
ENV PATH="/opt/venv/bin:$PATH"
COPY ./dist/*-py3-none-any.whl ./
RUN --mount=type=cache,target=/root/.cache/pip \
/usr/bin/env python3 -m pip install --force-reinstall ./*-py3-none-any.whl
ENTRYPOINT [ "/usr/bin/env", "python3" ]
CMD []