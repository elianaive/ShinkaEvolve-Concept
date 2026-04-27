# Redirect to owtn's canonical LLM dispatch. Generation calls (those with
# llm_context.role in {generation, genesis, mutation}) on registered models
# automatically fire the critique-revise cycle via owtn.optimizer.self_critic;
# everything else passes through unchanged.
from owtn.llm.api import query  # noqa: F401  (sync; non-generation only)
from owtn.optimizer.self_critic import query_async  # noqa: F401  (auto-gates self-critic)
