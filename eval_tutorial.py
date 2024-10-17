from braintrust import Eval
from autoevals import LevenshteinScorer
from dotenv import load_dotenv

load_dotenv()

Eval(
  "Say Hi Bot",
  data=lambda: [
      {
          "input": "Foo",
          "expected": "Hi Foo",
      },
      {
          "input": "Bar",
          "expected": "Hello Bar",
      },
  ],  # Replace with your eval dataset
  task=lambda input: "Hi " + input,  # Replace with your LLM call
  scores=[LevenshteinScorer],
)