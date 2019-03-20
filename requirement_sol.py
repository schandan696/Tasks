import subprocess

packagesDict = {
        'Dependencies' :[
        'beautifulsoup4==4.4.1',
        'boto==2.48.0',
        'bz2file==0.98',
        'certifi==2017.7.27.1',
        'chardet==3.0.4',
        'gensim==2.3.0',
        'html5lib==0.999',
        'idna==2.5',
        'nltk==3.2.4',
        'numpy==1.13.1',
        'pexpect==4.0.1',
        'pip==9.0.1',
        'ptyprocess==0.5',
        'pyxdg==0.25',
        'reportlab==3.3.0',
        'requests==2.18.3',
        'scipy==0.19.1',
        'setuptools==20.7.0',
        'six==1.10.0',
        'abccc',
        'smart-open==1.5.3',
        'textblob==0.12.0',
        'twitter==1.17.1',
        'xyz',
        'urllib3==1.22',
    ]
}
brokenPackage = []
for eachDependencies in packagesDict['Dependencies']:
    command = f'pip install {eachDependencies}'
    try:
        subprocess.run(command, shell=True, check=True)
        # if you don't want error to be printed do shell=False
    except Exception as e:
        print(f'Package broken or {eachDependencies} Dependencies missing')
        brokenPackage.append(eachDependencies)

print('there is some probleam in ', ','.join(brokenPackage), 'dependencies')
