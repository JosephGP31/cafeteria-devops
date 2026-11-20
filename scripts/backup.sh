#!/bin/bash
set -eo pipefail

mkdir -p backups
docker compose exec -T db pg_dump -U aroma_admin -d cafeteria_aroma > backups/respaldo_$(date +%Y%m%d_%H%M%S).sql
ls -1t backups/*.sql | tail -n +6 | xargs -r rm --