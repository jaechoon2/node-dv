{
  "targets": [
    {
      'target_name': 'libzxing',
      'type': 'static_library',
      'include_dirs': [
        'core/src',
      ],
      'sources': [
        'core/src/zxing/BarcodeFormat.cpp',
        'core/src/zxing/Binarizer.cpp',
        'core/src/zxing/BinaryBitmap.cpp',
        'core/src/zxing/DecodeHints.cpp',
        'core/src/zxing/Exception.cpp',
        'core/src/zxing/FormatException.cpp',
        'core/src/zxing/LuminanceSource.cpp',
        'core/src/zxing/MultiFormatReader.cpp',
        'core/src/zxing/NotFoundException.cpp',
        'core/src/zxing/Reader.cpp',
        'core/src/zxing/ReaderException.cpp',
        'core/src/zxing/Result.cpp',
        'core/src/zxing/ResultPoint.cpp',
        'core/src/zxing/ResultPointCallback.cpp',
        'core/src/zxing/aztec/AztecDetectorResult.cpp',
        'core/src/zxing/aztec/AztecReader.cpp',
        'core/src/zxing/aztec/decoder/1Decoder.cpp',
        'core/src/zxing/aztec/detector/1Detector.cpp',
        'core/src/zxing/common/Array.cpp',
        'core/src/zxing/common/BitArray.cpp',
        'core/src/zxing/common/BitMatrix.cpp',
        'core/src/zxing/common/BitSource.cpp',
        'core/src/zxing/common/CharacterSetECI.cpp',
        'core/src/zxing/common/Counted.cpp',
        'core/src/zxing/common/DecoderResult.cpp',
        'core/src/zxing/common/DetectorResult.cpp',
        'core/src/zxing/common/EdgeDetector.cpp',
        'core/src/zxing/common/GlobalHistogramBinarizer.cpp',
        'core/src/zxing/common/GreyscaleLuminanceSource.cpp',
        'core/src/zxing/common/GreyscaleRotatedLuminanceSource.cpp',
        'core/src/zxing/common/GridSampler.cpp',
        'core/src/zxing/common/HybridBinarizer.cpp',
        'core/src/zxing/common/IllegalArgumentException.cpp',
        'core/src/zxing/common/PerspectiveTransform.cpp',
        'core/src/zxing/common/Str.cpp',
        'core/src/zxing/common/StringUtils.cpp',
        'core/src/zxing/common/detector/1MonochromeRectangleDetector.cpp',
        'core/src/zxing/common/detector/WhiteRectangleDetector.cpp',
        'core/src/zxing/common/reedsolomon/GenericGF.cpp',
        'core/src/zxing/common/reedsolomon/GenericGFPoly.cpp',
        'core/src/zxing/common/reedsolomon/ReedSolomonDecoder.cpp',
        'core/src/zxing/common/reedsolomon/ReedSolomonException.cpp',
        'core/src/zxing/datamatrix/1Version.cpp',
        'core/src/zxing/datamatrix/DataMatrixReader.cpp',
        'core/src/zxing/datamatrix/decoder/1BitMatrixParser.cpp',
        'core/src/zxing/datamatrix/decoder/1DataBlock.cpp',
        'core/src/zxing/datamatrix/decoder/1DecodedBitStreamParser.cpp',
        'core/src/zxing/datamatrix/decoder/2Decoder.cpp',
        'core/src/zxing/datamatrix/detector/2Detector.cpp',
        'core/src/zxing/datamatrix/detector/2MonochromeRectangleDetector.cpp',
        'core/src/zxing/datamatrix/detector/CornerPoint.cpp',
        'core/src/zxing/datamatrix/detector/DetectorException.cpp',
        'core/src/zxing/multi/ByQuadrantReader.cpp',
        'core/src/zxing/multi/GenericMultipleBarcodeReader.cpp',
        'core/src/zxing/multi/MultipleBarcodeReader.cpp',
        'core/src/zxing/multi/qrcode/QRCodeMultiReader.cpp',
        'core/src/zxing/multi/qrcode/detector/MultiDetector.cpp',
        'core/src/zxing/multi/qrcode/detector/MultiFinderPatternFinder.cpp',
        'core/src/zxing/oned/Code128Reader.cpp',
        'core/src/zxing/oned/Code39Reader.cpp',
        'core/src/zxing/oned/EAN13Reader.cpp',
        'core/src/zxing/oned/EAN8Reader.cpp',
        'core/src/zxing/oned/ITFReader.cpp',
        'core/src/zxing/oned/MultiFormatOneDReader.cpp',
        'core/src/zxing/oned/MultiFormatUPCEANReader.cpp',
        'core/src/zxing/oned/OneDReader.cpp',
        'core/src/zxing/oned/OneDResultPoint.cpp',
        'core/src/zxing/oned/UPCAReader.cpp',
        'core/src/zxing/oned/UPCEANReader.cpp',
        'core/src/zxing/oned/UPCEReader.cpp',
        'core/src/zxing/qrcode/2Version.cpp',
        'core/src/zxing/qrcode/ErrorCorrectionLevel.cpp',
        'core/src/zxing/qrcode/FormatInformation.cpp',
        'core/src/zxing/qrcode/QRCodeReader.cpp',
        'core/src/zxing/qrcode/decoder/2BitMatrixParser.cpp',
        'core/src/zxing/qrcode/decoder/2DataBlock.cpp',
        'core/src/zxing/qrcode/decoder/2DecodedBitStreamParser.cpp',
        'core/src/zxing/qrcode/decoder/3Decoder.cpp',
        'core/src/zxing/qrcode/decoder/DataMask.cpp',
        'core/src/zxing/qrcode/decoder/Mode.cpp',
        'core/src/zxing/qrcode/detector/3Detector.cpp',
        'core/src/zxing/qrcode/detector/AlignmentPattern.cpp',
        'core/src/zxing/qrcode/detector/AlignmentPatternFinder.cpp',
        'core/src/zxing/qrcode/detector/FinderPattern.cpp',
        'core/src/zxing/qrcode/detector/FinderPatternFinder.cpp',
        'core/src/zxing/qrcode/detector/FinderPatternInfo.cpp',
        'core/src/zxing/qrcode/detector/QREdgeDetector.cpp',
      ],
      'cflags!': ['-fno-exceptions'],
      'cflags_cc!': ['-fno-exceptions'],
      'conditions': [
        ['OS=="mac"',
          {
            'xcode_settings': {
              'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
            }
          }
        ],
        ['OS=="win"',
          {
            'include_dirs': [
              'port',
            ],
            'sources': [
              'port/win_iconv.c',
            ],
            'configurations': {
              'Debug': {
                'msvs_settings': {
                  'VCCLCompilerTool': {
                    'ExceptionHandling': '1',
                  },
                },
              },
              'Release': {
                'msvs_settings': {
                  'VCCLCompilerTool': {
                    'ExceptionHandling': '1',
                  },
                },
              },
            },
          }
        ],
      ],
    },
  ]
}
