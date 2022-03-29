#!/usr/bin/env bash

set -e

project_wiki_url="https://gitlabe2.ext.net.nokia.com/api/v4/projects/41791/wikis"
modules="Configuration CustomNetworkProfile DeviceLocation Device GeoZone NetworkProfile"
base_page="Reference"

for module in $modules; do
    echo "Generating pydoc for $module module"
    content=$(poetry run pydoc-markdown -m network_as_code.${module} --render-toc)
    data="title=${base_page}/${module}&content=${content}"
    page_url="${project_wiki_url}/${base_page}%2F${module}"
    check_code=$(curl -s -o /dev/null -w "%{http_code}\n" --header "PRIVATE-TOKEN: $GITLAB_API_TOKEN" "$page_url")
    if [ $check_code = "200" ]; then
        echo "Updating existing page for $module module"
        curl -s --data "$data" --header "PRIVATE-TOKEN: $GITLAB_API_TOKEN" "$project_wiki_url" > /dev/null
    else
        echo "Creating new page for $module module"
        curl -s --request PUT --data "$data" --header "PRIVATE-TOKEN: $GITLAB_API_TOKEN" "$page_url" > /dev/null
    fi
done
