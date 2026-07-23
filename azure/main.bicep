param location string = resourceGroup().location
param containerAppName string = 'paper-draft-agent-app'
param acrName string = 'paperdraftacr'
param environmentName string = 'paper-draft-env'

@description('Container image (e.g. acrName.azurecr.io/paper-draft-agent:latest)')
param containerImage string

resource acr 'Microsoft.ContainerRegistry/registries@2023-01-01-preview' = {
  name: acrName
  location: location
  sku: {
    name: 'Basic'
  }
  properties: {
    adminUserEnabled: true
  }
}

resource env 'Microsoft.App/managedEnvironments@2023-05-01' = {
  name: environmentName
  location: location
  properties: {}
}

resource app 'Microsoft.App/containerApps@2023-05-01' = {
  name: containerAppName
  location: location
  properties: {
    managedEnvironmentId: env.id
    configuration: {
      ingress: {
        external: true
        targetPort: 8000
      }
    }
    template: {
      containers: [
        {
          name: 'paper-draft-agent'
          image: containerImage
          env: [
            {
              name: 'FOUNDRY_PROJECT_ENDPOINT'
              value: ''
            }
            {
              name: 'FOUNDRY_MODEL_NAME'
              value: 'gpt-4.1'
            }
          ]
        }
      ]
    }
  }
}

