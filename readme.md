# Whisper API 

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


This microservice is designed to handle audio transcription. Users can upload audio files, which are stored in a S3 bucket, and an event is published to a Kafka topic. A separate consumer service continuously reads messages from the topic and performs the transcription using OpenAI Whisper, aiming for a ~15-minute processing window.

## Technologies
- Audio Processing Library: [![FFmpeg](https://img.shields.io/badge/FFmpeg-0076B6?style=flat&logo=ffmpeg)](https://ffmpeg.org/)
- Speech-to-text Library: [![OpenAI Whisper](https://img.shields.io/badge/OpenAI-Whisper-blue)](https://beta.openai.com/)
- API Framework: [![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)
- Database: [![Postgres](https://img.shields.io/badge/Postgres-336791?style=flat&logo=postgresql)](https://www.postgresql.org/)
- Messaging Queue: [![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-231F20?style=flat&logo=apachekafka)](https://kafka.apache.org/)
- File Storage: [![S3](https://img.shields.io/badge/AWS-S3-orange?style=flat&logo=amazonaws)](https://aws.amazon.com/s3/)
- Containerization: [![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker)](https://www.docker.com/)


## Prerequisites
- Python 3.9+
- FFmpeg
- Docker

## Installation

1. Clone this repository:

   ```sh
   git clone https://github.com/conceptcodes/whisper-api-python.git
   cd whisper-api-python
   ```

2. Grab an API key from [Resend](https://resend.com/docs/introduction)

3. update your `.env` file

4. Start the application:

   ```sh
    make docker
   ```


## Roadmap
