# SpringBoot Workflow - Package Of Configuration Class

- add `@Configuration` at class level, to indicate that this is a configuration class
- Defined classes
  - MybatisConfiguration.java
    - Add `@MapperScan(val)` annotation to treat all interfaces in the specified package as Mapper interfaces
  - WebMvcConfiguration.java

## MybatisConfiguration.java

- Set the package where Mybatis interfaces are located

```java
@Configuration
@MapperScan("com.example.demo.mapper")  // Specify the package to search for mapper interfaces
public class MybatisConfiguration {
    public MybatisConfiguration() {
    }
}
```

## WebMvcConfiguration.java

- response [Cross-Origin resource sharing](http-cors.md)
- Override the addCorsMappings method

```java
@Configuration
public class WebMvcConfiguration implements WebMvcConfigurer {

    public WebMvcConfiguration() {
    }

    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/**")
                .allowedOriginPatterns("*")
                .allowedMethods("*")
                .allowedHeaders("*")
                .allowCredentials(true)
                .maxAge(3600);
    }

}
```

[Can be directly applied to the main class](springboot-cors-on-application.md)

## SecurityConfiguration.java

- Inherit from `WebSecurityConfigurerAdapter`
- Initialize Spring components
  - [AuthenticationManager](springsecurity-authenticationmanager-interface.md): Authentication manager
  - [PasswordEncoder](springsecurity-passwordencoder.md): Password encoder
- Override `configure(HttpSecurity http)`

```java
@Configuration
public class SecurityConfiguration extends WebSecurityConfigurerAdapter {

    @Bean
    public PasswordEncoder passwordEncoder() {
        // return NoOpPasswordEncoder.getInstance();
        return new BCryptPasswordEncoder();
    }

    @Bean
    @Override
    public AuthenticationManager authenticationManagerBean() throws Exception {
        return super.authenticationManagerBean();
    }

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        // Configure the HttpSecurity object
    }

    @Autowired
    JwtAuthorizationFilter jwtAuthorizationFilter;

}
```

Override Configure(HttpSecurity http)

- URLs allowed for access
- Allow [preflight requests](../../network/http-cors-preflighted-requests.md)
- Disable [csrf](web-csrf.md)
- Add filters

```java
protected void configure(HttpSecurity http) throws Exception {
    String[] urls = {
        // 授权可访问的url
    }

    http.authrizeRequests()
        .antMatchers(urls).permitAll()
        // Allow preflight requests
        .antMatchers(HttpMethod.OPTIONS, "/**").permitAll()
        .anyRequest().authenticated();


    // Disable csrf
    http.csrf().disable();  

    // Add token filter, before UsernamePasswordAuthenticationFilter
    http.addFilterBefore(jwtAuthorizationFilter, UsernamePasswordAuthenticationFilter.class);

    // Allow cross-origin
    http.cors();
}
```

## RedisConfiguration.java

## ScheduleConfiguration.java

- Use the `@EnableScheduling` annotation in the configuration class to **enable scheduled tasks**

> No need to add other methods

```java
@Configuration
@EnableScheduling
public class ScheduleConfiguration {

    public ScheduleConfiguration() {
        // ScheduleConfiguration loaded message
    }
```

## DataSourceConfiguration.java

Annotations for configuration classes

```java
@MapperScan(
    basePackages = "com.example.demo.mapper",
    sqlSessionTemplateRef = "db1sqlSessionTemplate"
    )
```

- `@MapperScan`: Specify the package where mapper interfaces are located
- `sqlSessionTemplateRef`: Specify the bean name of SqlSessionTemplate

Annotations for class methods

- Use the `@ConfigurationProperties(prefix = "spring.datasource.first")` annotation to read configuration from the config file
- Use the `@Bean` annotation to create a DataSource instance

> The SqlSessionTemplate instance is assembled by the [Mapper](springboot-project-workflow-mapper.md) interface


```java
@Configuration
@MapperScan(basePackages = "com.example.project_name.business.mapper.first", sqlSessionTemplateRef = "FirstSqlSessionTemplate")
public class FirstDataSourceConfiguration {
    /**
     * Generate data source. The @Primary annotation declares it as the default data source
     */
    @Bean(name = "firstDataSource")
    @ConfigurationProperties(prefix = "spring.datasource.first")
    @Primary
    public DataSource testDataSource() {
        return DataSourceBuilder.create().build();
    }

    /**
     * Create SqlSessionFactory
     */
    @Bean(name = "firstSqlSessionFactory")
    @Primary
    public SqlSessionFactory testSqlSessionFactory(@Qualifier("firstDataSource") DataSource dataSource) throws Exception {
        SqlSessionFactoryBean bean = new SqlSessionFactoryBean();
        bean.setDataSource(dataSource);
        // Set the path for mybatis mapper files
        bean.setMapperLocations(new PathMatchingResourcePatternResolver().getResources
                ("classpath:mapper/first/*.xml"));
        return bean.getObject();
    }

    /**
     * Configure transaction management
     */
    @Bean(name = "firstTransactionManager")
    @Primary
    public DataSourceTransactionManager testTransactionManager(@Qualifier("firstDataSource") DataSource dataSource) {
        return new DataSourceTransactionManager(dataSource);
    }

    @Bean(name = "firstSqlSessionTemplate")
    @Primary
    public SqlSessionTemplate testSqlSessionTemplate(@Qualifier("firstSqlSessionFactory") SqlSessionFactory sqlSessionFactory) throws Exception {
        return new SqlSessionTemplate(sqlSessionFactory);
    }
}
```

