from setuptools import setup, find_packages

setup(**{
    'name': 'scalable_chat',
    'version': '0.1-dev',
    'author': 'Alexey Poryadin',
    'author_email': 'alexey.poryadin@gmail.com',
    'description': 'Scalable chat',
    'packages': find_packages(),
    'install_requires': [
        'tornado', 'aioredis'
    ]
})
