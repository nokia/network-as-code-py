#!/usr/bin/env bash

project_wiki_url="https://gitlabe2.ext.net.nokia.com/api/v4/projects/41791/wikis"
modules="Configuration CustomNetworkProfile DeviceLocation Device GeoZone NetworkProfile"
base_page="Reference"

for module in $modules; do
    content="title=${base_page}/${module}&content=$(poetry run pydoc-markdown -m network_as_code.${module} --render-toc)"
    page_url="${project_wiki_url}/${base_page}%2F${module}"
    check_code=$(curl -s -o /dev/null -w "%{http_code}\n" --header "PRIVATE-TOKEN: $GITLAB_API_TOKEN" $page_url)
    if [ $check_code = "200" ]; then
        curl --request PUT --data $content --header "PRIVATE-TOKEN: $GITLAB_API_TOKEN" $page_url
    else
        curl --data $content --header "PRIVATE-TOKEN: $GITLAB_API_TOKEN" $project_wiki_url
    fi
done
