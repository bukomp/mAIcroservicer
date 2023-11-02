#!/bin/bash
vulture ./src --min-confidence 60 --exclude microservices/ --sort-by-size | grep -v "unused property" | grep -v "unused attribute"
