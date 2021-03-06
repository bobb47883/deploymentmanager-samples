# Copyright 2018 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
""" Creates a runtimeConfig variable resource. """


def generate_config(context):
    """ Entry point for the deployment resources. """

    name = context.properties.get('variable', context.env['name'])
    config_name = context.properties.get('config')
    required_properties = ['parent', 'variable']
    optional_properties = ['text', 'value']
    # Load the required properties, then the optional ones if specified.
    properties = {p: context.properties[p] for p in required_properties}
    properties.update({
        p: context.properties[p]
        for p in optional_properties if p in context.properties
    })

    resources = [{
        'name': name,
        'type': 'runtimeconfig.v1beta1.variable',
        'properties': properties,
        'metadata': {
            'dependsOn': [config_name]
        }
    }]

    outputs = [{
        'name': 'updateTime',
        'value': '$(ref.{}.updateTime)'.format(name)
    }]

    return {'resources': resources, 'outputs': outputs}
