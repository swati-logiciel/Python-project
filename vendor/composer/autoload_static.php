<?php

// autoload_static.php @generated by Composer

namespace Composer\Autoload;

class ComposerStaticInit6e03a8082adb78a8c5be948426ac16a3
{
    public static $prefixLengthsPsr4 = array (
        'G' => 
        array (
            'Grpc\\' => 5,
        ),
    );

    public static $prefixDirsPsr4 = array (
        'Grpc\\' => 
        array (
            0 => __DIR__ . '/..' . '/grpc/grpc/src/lib',
        ),
    );

    public static $classMap = array (
        'Composer\\InstalledVersions' => __DIR__ . '/..' . '/composer/InstalledVersions.php',
    );

    public static function getInitializer(ClassLoader $loader)
    {
        return \Closure::bind(function () use ($loader) {
            $loader->prefixLengthsPsr4 = ComposerStaticInit6e03a8082adb78a8c5be948426ac16a3::$prefixLengthsPsr4;
            $loader->prefixDirsPsr4 = ComposerStaticInit6e03a8082adb78a8c5be948426ac16a3::$prefixDirsPsr4;
            $loader->classMap = ComposerStaticInit6e03a8082adb78a8c5be948426ac16a3::$classMap;

        }, null, ClassLoader::class);
    }
}