from setuptools import setup, find_packages


def readme():
    with open("README.md") as f:
        return f.read()



classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='animerem',
  version='0.0.1',
  description='A simle package to scrap anime infos ',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url="https://github.com/petanon/animerem",
  author='alaa petanon',
  author_email='kofdjka@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='anime scrapper', 
  packages=find_packages(),
  install_requires=["lxml","requests","asyncio"] 
)
