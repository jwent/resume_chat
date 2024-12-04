$apiKey = $env:OPENAI_API_KEY

# Check if the API key exists
if (-not $apiKey) {
    Write-Error "API key not found. Set the 'OPENAI_API_KEY' environment variable."
    exit 1
}

$projectId = $env:PROJECT_ID

# Check if the API key exists
if (-not $projectId) {
    Write-Error "Project ID key not found. Set the 'PROJECT_ID' environment variable."
    exit 1
}

$apiUrl = "https://api.openai.com/v1/models"
$headers = @{
    "Authorization" = "Bearer $env:OPENAI_API_KEY"
    "OpenAI-Organization" = $env:OPENAI_ORG
    "OpenAI-Project" = $env:PROJECT_ID
}

# Make the API request
$response = Invoke-RestMethod -Uri $apiUrl -Headers $headers -Method Get

# Output the model details
$response.data | ForEach-Object {
    Write-Output "Model ID: $($_.id)"
    Write-Output "Created: $($_.created)"
    Write-Output "Owned By: $($_.owned_by)"
    Write-Output "Version: $($_.id)"  # Assuming the model ID contains version info
    Write-Output "-----------------------------"
}
