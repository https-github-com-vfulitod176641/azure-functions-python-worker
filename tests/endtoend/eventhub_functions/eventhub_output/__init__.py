# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
import azure.functions as func


def main(req: func.HttpRequest, event: func.Out[str]):
    event.set(req.get_body().decode('utf-8'))

    return 'OK'
