# -*- coding: utf-8 -*-

import os, zipfile, tempfile, shutil, scrapy
import scrapy.exceptions
import scrapy.pipelines.files as scrapy_pipelines
import scrapy.utils.project as scrapy_project

class VoterListPipeline(scrapy_pipelines.FilesPipeline):
    FILES_URLS_FIELD   = 'file_url'
    FILES_RESULT_FIELD = 'file_data'

    def get_media_requests(self, item, info):
        file_url = item.get(self.files_urls_field)
        print(u'  Downloading list file at:            %s…' % file_url)

        # TODO (PJ): Here it might be good to break out of the whole
        #   default Scrapy way of doing things. Either way, it'd be
        #   nice to see:
        #     - that the download is progressing or failing, and a
        #     - progress bar of download

        yield scrapy.Request(file_url, meta={
            'ftp_user':     'anonymous',
            'ftp_password': ''
        })

    def item_completed(self, results, item, info):
        if not (isinstance(item, dict) or self.files_result_field in item.fields):
            return item # Skip

        # Grab all of the file_data from each result returned, and
        #   since we are only requesting a single result, grab it…
        item[self.files_result_field] = [x for ok, x in results if ok]
        item[self.files_result_field] = item[self.files_result_field][0]


        input_file_name, output_file_name, input_path, output_path = \
          self.resolve_file_names(item)

        # Unzip if necessary.
        if input_file_name.endswith('.zip'):
            print(u'  File downloaded to /data with path:  %s…' % input_file_name)
            print(u'  Unzipping to:                        %s…' % output_file_name)

            self.unzip_file(input_path, output_path)
        else:
            print(u'  File downloaded to /data with path:  %s.' % input_file_name)

        print(u'  Complete! Moving on.\n')
        return item


    def resolve_file_names(self, item):
        input_file_name  = item[self.files_result_field]['path']
        output_file_name = os.path.join('full', item.file_name())

        data_dir  = scrapy_project.get_project_settings().get('DATA_DIR')

        input_path  = os.path.join(data_dir, input_file_name)
        output_path = os.path.join(data_dir, output_file_name)

        return (input_file_name, output_file_name, input_path, output_path)


    def unzip_file(self, input_path, output_path):
        # FIXME (PJ): Should use a context manager, a la
        #   http://stackoverflow.com/a/22726782, but not available
        #   as of 2.7, and don't feel like dropping in all the code
        #

        tmp_dir = tempfile.mkdtemp()

        with zipfile.ZipFile(input_path, 'r') as zipped_voter_list:
            member = zipped_voter_list.namelist()[0]
            zipped_voter_list.extract(member, tmp_dir)

        tmp_file = os.path.join(tmp_dir, member)

        if os.path.isfile(tmp_file):
            shutil.move(tmp_file, output_path)
            os.remove(input_path)
            print(u'  Deleting zip file…')

        shutil.rmtree(tmp_dir)


