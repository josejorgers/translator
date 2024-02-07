# File Translator

This is an simple translator that uses OpenAI's LLMs.

## Development

We recommend using Docker for the development process. You can run:

```bash
docker build -t translator-dev -f Dockerfile.dev .
docker run -it -d -v .:/code translator-dev
```

It will create a docker container that has everything needed to the development process. After that you can work inside that container, for example using the Dev Containers extension in VSCode.

In Linux, you can use ```make``` instead of the previous commands:

```bash
make build-dev
make run-dev
```

Make sure to create a file called ```.env``` at the root level, containing the following env variables:

```bash
OPENAI_API_KEY=<YOUR OPENAI API KEY>
INPUT_DIR=<AN EXISTING DIRECTORY TO GET THE INPUT FILES FROM>
OUTPUT_DIR=<AN EXISTING DIRECTORY TO WRITE THE TRANSLATIONS TO>
INPUT_LANG=<LANGUAGE IN THE INPUT. Ex: Spanish>
OUTPUT_LANG=<LANGUAGE IN THE INPUT. Ex: English>
CHUNK_SIZE=<SIZE OF EACH CHUNK TO TRANSLATE. Ex: 100>
```

Once inside the container, you can run tests by running:

```bash
pytest
```

## Execution

To execute the project you need to create the ```.env``` file as explained above. Then you can run:

```bash
docker build -t translator .
docker run -v .:/code translator
```

In Linux you can use ```make``` instead:

```bash
make build
make run
```

This will translate every file in the ```INPUT_DIR``` and write the translation into files with the same name but into the ```OUTPUT_DIR```.

## Prompt Customization

Currently the prompt to make the translations is hardcoded in the ```./src/translator.py``` file. Modify it according to your necessities.

## Contribute

Please feel free to fork this repo. Also, feel free to add issues, open PRs, and contribute in any way you consider useful. I wrote this simple code to translate a book of mine. I didn't intended to make it public, but here we are. There is room for improvement for sure and I'll be happy to collaborate with anyone that think this can help others.

Happy Translation!
