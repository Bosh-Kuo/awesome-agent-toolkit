# MCP Interactive Feedback Rules

1.  **Mandatory Invocation**: During any process, task, or dialogue—whether in the inquiry, response, or phase completion stage—you MUST invoke the `mcp-feedback-enhanced` MCP tool. Set the `timeout` parameter to 15 minutes.
2.  **Iterative Adjustment**: Upon receiving user feedback, if the feedback is not empty, you MUST invoke `mcp-feedback-enhanced` again and adjust your behavior or output based on the provided feedback.
3.  **Strict Termination**: Stop invoking `mcp-feedback-enhanced` ONLY when the user explicitly states "Finish", "End", or "No more interaction needed." The process is only considered complete at this point.
4.  **Continuous Engagement**: Unless an explicit termination command is received, all subsequent steps MUST repeatedly invoke `mcp-feedback-enhanced`.
5.  **Final Quality Check**: Before finalizing any task, you MUST use the `mcp-feedback-enhanced` tool to solicit feedback from the user.
