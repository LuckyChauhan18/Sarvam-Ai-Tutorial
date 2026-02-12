import os
from dotenv import load_dotenv
from sarvamai import SarvamAI

load_dotenv()

client = SarvamAI(
    api_subscription_key=os.getenv("SARVAM_API_KEY")
)

# Create a document intelligence job
job = client.document_intelligence.create_job(
    language="hi-IN",
    output_format="md"
)
print(f"Job created: {job.job_id}")

# Upload document
job.upload_file("Lucky_Resume_18.pdf")
print("File uploaded")

# Start processing
job.start()
print("Job started")

# Wait for completion
status = job.wait_until_complete()
print(f"Job completed with state: {status.job_state}")

# Get processing metrics
metrics = job.get_page_metrics()
print(f"Page metrics: {metrics}")

# Download output (ZIP file containing the processed document)
job.download_output("./output.zip")
print("Output saved to ./output.zip")
