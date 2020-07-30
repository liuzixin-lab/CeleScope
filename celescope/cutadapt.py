# -*- coding: utf-8 -*-
import sys

import re
from .report import Reporter
from .utils import getlogger, CommandWrapper

logger = getlogger(__name__)
logger.setLevel(10)


class CutadaptLogger(object):
    def __init__(self, stdout, sample):
        self.stdout = stdout
        self.sample = sample
        self.stat_info = {
            'visible': {},
            'invisible': {}
        }
        self.parse()

    def parse(self):
        pattern = re.compile(r'(Total reads processed:.*?Total written.*?)\n', flags=re.S)
        pattern_space = re.compile(r':\s*')
        match = pattern.search(self.stdout)
        if match:
            for line in match.group().splitlines():
                if line:
                    line = re.sub(pattern_space, ':', line)
                    line = line.replace(',', '')
                    attr, val = line.split(':')
                    self.stat_info['visible'][attr] = val
        else:
            logger.warning(f'can not match cutadapt log')


def cutadapt(ctx, fq, sample, outdir, adapter, minimum_length, nextseq_trim, overlap, thread, debug):
    adapter_para = ''
    for i, j in zip(['-a'] * len(adapter), adapter):
        adapter_para += f'{i} {j} '
    sample_outdir = outdir / sample / '02.cutadapt'
    sample_outdir.mkdir(parents=True, exist_ok=True)

    # cutadapt
    clean_fastq = sample_outdir / f'{sample}_clean_2.fq.gz'
    cutadapt_cmd = f'cutadapt {adapter_para}-n {len(adapter)} -j {thread} -m {minimum_length} --nextseq-trim={nextseq_trim} --overlap {overlap} -o {clean_fastq} {fq}'
    logger.info('cutadapt start!')
    logger.info(cutadapt_cmd)
    cutadapt_process = CommandWrapper(command=cutadapt_cmd, logger=logger)
    if cutadapt_process.returncode:
        logger.warning('cutadapt error!')
        sys.exit(-1)
    else:
        logger.info('cutadapt done!')

    # parse log
    cutadapt_log = CutadaptLogger(stdout=cutadapt_process.stdout, sample=sample)

    # report
    logger.info('generate report start!')
    Reporter(name='cutadapt', stat_json=cutadapt_log.stat_info, outdir=sample_outdir.parent)
    logger.info('generate report done!')
