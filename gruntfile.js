module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    bower_concat: {
      all: {
        dest: {
          'js':  'django_sb_admin_ssx/static/js/_bower.js',
          'css': 'django_sb_admin_ssx/static/css/_bower.css',
        },
        dependencies:{
          'bootstrap' : 'jquery',
          'flot' : 'jquery'
        },
        mainFiles: {
          'font-awesome' : ['css/font-awesome.min.css'],
          'bootstrap' : ['dist/css/bootstrap.min.css', 'dist/css/bootstrap-theme.min.css']
        },
        bowerOptions: {
          relative: false
        }
      }
    },
    copy:{
      files:[
        {
          src: 'bower_components/bootstrap/dist/fonts/*',
          dest: 'django_sb_admin_ssx/static/fonts/'
        },
        {
          src: 'bower_components/font-awesome/fonts/*',
          dest: 'django_sb_admin_ssx/static/fonts/'
        }]
    }
  });


  // Load the plugins that provides the "bower_concat" and "copy" tasks.
  grunt.loadNpmTasks('grunt-bower-concat');
  grunt.loadNpmTasks('grunt-contrib-copy');

  // Default task(s).
  grunt.registerTask('default', ['bower_concat', 'copy']);
};

// Load the plugin that provides the "uglify" task.
// grunt.loadNpmTasks('grunt-contrib-uglify');
/*add to 'default' tasks list 'uglify',*/
// uglify: {
//   options: {
//     banner: '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n'
//   },
//   build: {
//     src: 'src/<%= pkg.name %>.js',
//     dest: 'build/<%= pkg.name %>.min.js'
//   },
// },
