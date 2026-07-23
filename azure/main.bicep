name: paper-draft-agent
metadata:
  template: paper-draft-agent

services:
  agent:
    project: ../
    language: python
    host:
      type: containerapp
    docker:
      path: ../Dockerfile
      context: ../
    resourceGroup: paper-draft-agent-rg
    environment: paper-draft-agent-env
