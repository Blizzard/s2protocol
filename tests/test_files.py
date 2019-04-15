import unittest
import mpyq
import os
from s2protocol import versions

self_path = os.path.dirname(__file__)

class FilesTestCase(unittest.TestCase):
    def test_files(self):
        test_data_dir = 's2replaystatsdata'
        for test_file in os.listdir(os.path.join(self_path, test_data_dir)):
            self.process_sing_file(os.path.join(self_path, test_data_dir, test_file))

    def process_sing_file(self, replay_file_name):
        archive = mpyq.MPQArchive(replay_file_name)
        contents = archive.header['user_data_header']['content']
        header = versions.latest().decode_replay_header(contents)

        base_build = header['m_version']['m_baseBuild']
        try:
            protocol = versions.build(base_build)
        except Exception as e:
            self.fail('Unsupported base build: {0} ({1!s})'.format(base_build, e))

        required_internal_files = ['replay.details',
                          'replay.details.backup',
                          'replay.initData',
                          'replay.game.events',
                          'replay.message.events',
                          'replay.tracker.events'
        ]

        for internal_file_name in required_internal_files:
            contents = archive.read_file(internal_file_name)
            self.assertIsNotNone(contents)

            # just decode init data
            if internal_file_name is 'replay.initData':
                result = protocol.decode_replay_initdata(contents)
                self.assertIsNotNone(result)
        print('processed {}, base_build: {}'.format(replay_file_name, base_build))


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(FilesTestCase)
