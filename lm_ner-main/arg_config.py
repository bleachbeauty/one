
import random

class Config(object):

    def __init__(self):
        
        self.mode = 'train'                     # train/eval/test
        self.continue_train = False             # 是否继续训练上次的模型
        # self.multi_gpu = False
        self.visible_device = '0'
        self.device = 'cuda:0'
        self.model_name = 'KoichiYasuoka/roberta-classical-chinese-large-char_crf'         
        self.language = 'en'

        self.model_list_nopretrain = ['lstm_crf', 'transformer']
        self.model_list_pretrain = ['albert_crf', 'bert_crf', 'roberta_crf']
        self.model_pretrain_online_checkpoint = 'KoichiYasuoka/roberta-classical-chinese-large-char'     #'albert-base-v2'
        #self.model_pretrain_online_checkpoint = 'D:\PTM\roberta-classical-chinese-base-char'
        # 这个路径在哪？
        self.model_pretrain_trainable = True

        # data
        self.dataset = 'CNER'
        self.path_dataset = './dataset/'+ self.dataset +'/'
        self.path_output = './dataset/'+ self.dataset +'/output.txt'

        # base model
        self.path_base = './checkpoints/' + self.dataset
        self.path_tokenizer = self.path_base + '/tokenizer/'
        # self.path_bert = './checkpoints/'
        self.path_model = self.path_base + '/model/'
        self.path_optimizer = self.path_base + '/optimizer/'
        
        # model parameter
        self.learning_rate = 3e-5
        self.crf_learning_rate = 5e-3
        self.warmup_proportion = 0.1            # warm up的步数比例x（全局总训练次数t中前x*t步）
        self.weight_decay = 0.01                # 权重衰减的比例
        self.adam_epsilon = 1e-08

        # training
        self.epoch = 2800
        self.step_save = 2000
        self.batch_size = 48
        self.max_seq_length = 512
        # self.path_save_model = './checkpoints/bert_crf/'
        self.path_tgt_map = './dataset/'+ self.dataset +'/map.txt'
        self.path_vocab = './dataset/'+ self.dataset +'/vocab.pkl'

        # 多卡训练配置
        # self.init_method = 'tcp://localhost:21339'
        self.port = str(random.randint(10000,60000))                # 多卡训练进程间通讯端口
        self.init_method = 'tcp://localhost:' + self.port           # 多卡训练的通讯地址


        # tag type
        # self.tag_type = ['ORG', 'RACE', 'PRO', 'NAME', 'EDU', 'CONT', 'LOC', 'TITLE']
        # self.tag_method = 'BMES'     # B IO
        # self.tag_type = ['ORG', 'LOC']
        # self.tag_method = 'BIO'     # BIO


        # pretrain model
        self.pretrain_model = [
            'bert-base-chinese',                                # BERT: Google开源中文预训练模型（12-layer, 768-hidden, 12-heads, 110M parameters）
            'hfl/chinese-bert-wwm',                             # BERT: 中文wiki数据训练的Whole Word Mask版本（12-layer, 768-hidden, 12-heads, 110M parameters）
            'hfl/chinese-bert-wwm-ext',                         # BERT: 使用额外数据训练的Whole Word Mask版本（12-layer, 768-hidden, 12-heads, 110M parameters）
            'hfl/chinese-roberta-wwm-ext',                      # RoBERTa: 使用额外数据训练的Whole Word Mask版本（12-layer, 768-hidden, 12-heads, 110M parameters）
            'hfl/chinese-roberta-wwm-ext-large',                # RoBERTa: 使用额外数据训练的Whole Word Mask+Large 版本（24-layer, 1024-hidden, 16-heads, 330M parameters）
            'voidful/albert_chinese_base',                      # Albert: 非官方+base版（12layer）
            'voidful/albert_chinese_large',                     # Albert: 非官方+large版（24layer）
            'hfl/chinese-electra-base-discriminator',           # ELECTRA: 中文版+discriminator（12层，隐层768，12个注意力头，学习率2e-4，batch256，最大长度512，训练1M步）
            'hfl/chinese-electra-large-discriminator',          # ELECTRA: 中文版+discriminator+large （24层，隐层1024，16个注意力头，学习率1e-4，batch96，最大长度512，训练2M步）
            'hfl/chinese-electra-180g-base-discriminator',      # ELECTRA: 中文版+discriminator+大训练语料（12层，隐层768，12个注意力头，学习率2e-4，batch256，最大长度512，训练1M步）
            'hfl/chinese-electra-180g-large-discriminator',     # ELECTRA: 中文版+discriminator+大训练语料+large （24层，隐层1024，16个注意力头，学习率1e-4，batch96，最大长度512，训练2M步）
            'KoichiYasuoka/roberta-classical-chinese-large-char',
        ]
        
        ## 中文模型出处：
        # bert: https://github.com/huggingface/transformers
        # bert-wwm/roberta: https://github.com/ymcui/Chinese-BERT-wwm
        # albert: https://github.com/brightmart/albert_zh
        # electra: https://github.com/ymcui/Chinese-ELECTRA

