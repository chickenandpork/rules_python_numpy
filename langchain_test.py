from langchain.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from os import environ
import unittest


def cachedir():
    if "TEST_TMPDIR" in environ:
        return "{}/{}".format(environ.get("TEST_TMPDIR"), "llm")
    if "TMPDIR" in environ:
        return "{}/{}".format(environ.get("TMPDIR"), "llm")

    return None


def gen_llm():
    proxies = dict()
    if "HTTP_PROXY" in environ:
        proxies.update({"http": environ.get("HTTP_PROXY")})
    if "HTTPS_PROXY" in environ:
        proxies.update({"https": environ.get("HTTPS_PROXY")})

    print("cachedir: {}".format(cachedir()))
    print("proxies: {}".format(proxies))

    return HuggingFacePipeline.from_model_id(
        model_id="bigscience/bloom-1b7",
        model_kwargs={
            "temperature": 0,
            "max_length": 64,
            "cache_dir": cachedir(),
            "proxies": proxies,
        },
        task="text-generation",
    )


template = """Question: {question}

Answer: Let's think step by step."""


def infer(question: str) -> str:
    prompt = PromptTemplate.from_template(template)

    chain = prompt | gen_llm()
    return chain.invoke({"question": question})


class DoesLangChainStandupTest(unittest.TestCase):
    @unittest.skipIf(
        "HTTPS_PROXY" not in environ,
        "test chews too much data without a federated caching-proxy",
    )
    def test_inference(self):
        answer = infer("What is prestidigitation?")

        self.assertIsNotNone(answer)
        # self.assertIsNotNone(m.dimensions)

        # self.assertEqual(m.dimensions, (10,20))


if __name__ == "__main__":
    unittest.main()
