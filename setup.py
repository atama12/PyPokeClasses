from setuptools import setup, find_packages

setup(
    name="pokeAPI_Models",  # パッケージ名
    version="0.1.0",  # バージョン
    author="Atama12",  # 作者名
    author_email="atama5860@gmail.com",  # メールアドレス
    description="A class-based Package for accessing and interacting with PokeAPI's JSON data.",  # パッケージの説明
    long_description=open("README.md", "r").read(),  # 長い説明（READMEから）
    long_description_content_type="text/markdown",  # READMEのフォーマット（markdownの場合）
    url="https://github.com/atama12/pokeAPI_Models.git",  # リポジトリのURL
    packages=find_packages(),  # パッケージを自動で探してくれる
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',  # 対応するPythonのバージョン
    install_requires=[
        "requests",  # 必要なパッケージ
        "typing",
        "json",
        
    ],
)
