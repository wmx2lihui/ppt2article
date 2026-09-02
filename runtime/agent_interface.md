# Agent Interface Specification

Every agent receives:

- research_memory
- current_task
- target_journal
- style_profile
- previous_feedback

Every agent returns:

- analysis
- generated_artifacts
- confidence
- next_actions

Agents communicate through structured memory rather than raw chat history.
