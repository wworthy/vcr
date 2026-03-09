# System Architecture — MediaMinds VCR

## Hosting & domain

- Domain: `vcr.mediamindsai.xyz`
- DNS: Route53
- Compute: AWS EC2
- Database: AWS RDS PostgreSQL (`mediaminds_vcr`)
- Object storage: S3 bucket `mediaminds-vcr`

## Runtime layers

1. Nginx reverse proxy
2. Angular frontend
3. FastAPI backend (`/api`)
4. PostgreSQL persistence
5. S3 for crawler outputs and reports

## Server structure

- `/opt/vcr/backend`
- `/opt/vcr/frontend`
- `/opt/vcr/workers`
- `/opt/vcr/scripts`
- `/opt/vcr/logs`

## Backend endpoints (initial)

- `GET /clients`
- `GET /clients/{uuid}`
- `POST /clients`
- `GET /clients/{uuid}/competitors`
- `GET /clients/{uuid}/vcr`
- `GET /clients/{uuid}/velocity`
- `GET /clients/{uuid}/content-opportunities`
- `POST /clients/{uuid}/crawler/run`
- `GET /clients/{uuid}/crawler/status`
- `POST /clients/{uuid}/generate-strategy`

## Database tables (planned)

- `clients`
- `competitors`
- `competitor_platforms`
- `competitor_rankings`
- `competitor_snapshots`
- `social_metrics`
- `keywords`
- `content_opportunities`
- `vcr_reports`

## S3 object layout

- `clients/{uuid}/crawler/discovery/`
- `clients/{uuid}/crawler/snapshots/`
- `clients/{uuid}/crawler/screenshots/`
- `clients/{uuid}/reports/`
- `clients/{uuid}/analysis/`

## Worker services

- `competitor_discovery_worker`
- `social_velocity_worker`
- `keyword_monitor_worker`
- `ai_visibility_worker`
- `content_gap_worker`

Executed via cron and/or Celery queues.
